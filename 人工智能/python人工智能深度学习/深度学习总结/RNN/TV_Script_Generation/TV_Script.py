from TV_Script_Generation import helper
import numpy as np
import warnings
from tensorflow.contrib import seq2seq
import tensorflow as tf

data_dir = 'moes_tavern_lines.txt'

# 数据读取和数据预处理
def read_data_and_preprocess():
    data_dir = 'moes_tavern_lines.txt'
    text = helper.load_data(data_dir)
    # 去除剧本开头的版权说明。
    text = text[81:]
    print('该剧本长度：%d' % len(text))

    # 探索数据集
    view_sentence_range = (0, 100)
    print('数据集统计信息')
    print('唯一单词的数量: {}'.format(len({word:None for word in text.split()})))
    scenes = text.split('\n\n')
    print('场景数量为: {}'.format(len(scenes)))
    sentence_count_scene = [scene.count('\n') for scene in scenes]
    print('每个场景平均句子数量: {}'.format(np.average(sentence_count_scene)))

    sentences = [sentence for scene in scenes for sentence in scene.split('\n')]
    print('句子总数量为: {}'.format(len(sentences)))
    word_count_sentence = [len(sentence.split()) for sentence in sentences]
    print('每句的平均单词数量: {}'.format(np.average(word_count_sentence)))

    print()
    print('The sentences {} to {}:'.format(*view_sentence_range))
    print('\n'.join(text.split('\n')[view_sentence_range[0]:view_sentence_range[1]]))


# 把word，id以dict的形式存储
def create_lookup_tables(text):
    """
    Create lookup tables for vocabulary
    :param text: The text of tv scripts split into words
    :return: A tuple of dicts (vocab_to_int, int_to_vocab)
    """
    # todo 需要编程：
    words = sorted(list(set(text)))
    vocab_to_int = {word:idx for idx, word in enumerate(words)}
    int_to_vocab = dict(enumerate(words))
    return vocab_to_int, int_to_vocab


# 标点符号代替符
"""
"!" 转换成： "||Exclamation_Mark||"。key值是标点符号，value是替代的文本。 
- Period ( . )
- Comma ( , )
- Quotation Mark ( " )
- Semicolon ( ; )
- Exclamation mark ( ! )
- Question mark ( ? )
- Left Parentheses ( ( )
- Right Parentheses ( ) )
- Dash ( -- )
- Return ( \n )
"""


def token_lookup():
    """
    Generate a dict to turn punctuation into a token.
    :return: Tokenize dictionary where the key is the punctuation and the value is the token
    """
    token_dict = {'.':'||Period||', ', ':'||Comma||', '"':'||Quotation_Mark||', ';':'||Semicolon||',
                  '!':'||Exclamation_mark||', '?':'||Question_mark||', '(':'||Left_Parentheses||',
                  ')':'||Right_Parentheses||', '--':'||Dash||', '\n':'||Return||'}
    return token_dict


# 预处理数据(并生成 训练 验证 和测试数据。)，并保存本地
def preprocess_and_save_data():
    helper.preprocess_and_save_data(data_dir, token_lookup, create_lookup_tables)


int_text, vocab_to_int, int_to_vocab, token_dict = helper.load_preprocess()


'''
    构建网络：
        get_inputs
        get_init_cell
        get_embed
        build_rnn
        build_nn
        get_batches
'''
def get_inputs():
    """
    为input, targets, and learning rate 创建占位符
    :return: Tuple (input, targets, learning rate)
    """
    inputs = tf.placeholder(tf.int32, [None, None], name='input')
    targets = tf.placeholder(tf.int32, [None, None], name='targets')
    learning_rate = tf.placeholder(tf.float32)
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')
    return inputs, targets, learning_rate, keep_prob


# todo Build RNN Cell and Initialize
"""
1\堆栈一个或者多个[`BasicLSTMCells`]
2\再使用函数[`tf.identity()`],初始化状态，并命名为："initial_state"
Return ： `(Cell, InitialState)`
"""


def get_init_cell(batch_size, rnn_size, keep_prob, lstm_layers=2):
    """
    Create an RNN Cell and initialize it.
    :param batch_size: Size of batches
    :param rnn_size: Size of RNNs
    :return: Tuple (cell, initialize state)
    """
    def build_cell(lstm_size, keep_prob):
        cell = tf.contrib.rnn.BasicLSTMCell(num_units=lstm_size)
        drop = tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=keep_prob)
        return drop

    # 堆栈cell 构建多层隐藏层
    multi_cell = tf.contrib.rnn.MultiRNNCell(
        [build_cell(rnn_size, keep_prob) for _ in range(lstm_layers)]
    )

    # todo 这里使用tf.identity(final_state同)是为了生成一个op操作符，断点继续训练时候要用。
    initial_state = multi_cell.zero_state(batch_size, tf.float32)
    initial_state1 = tf.identity(initial_state, name='initial_state')
    return multi_cell, initial_state, initial_state1


# todo 单词嵌入-对`input_data`应用单词嵌入；返回 嵌入序列
def get_embed(input_data, vocab_size, embed_dim):
    """
    Create embedding for <input_data>.
    :param input_data: TF placeholder for text input.
    :param vocab_size: Number of words in vocabulary.
    :param embed_dim: Number of embedding dimensions
    :return: Embedded input.
    """
    # todo 需要编程：
    # 1、构建嵌入矩阵的查找表
    lookup_w = tf.Variable(
        initial_value=tf.random_uniform([vocab_size, embed_dim], -1.0, 1.0)
    )
    # 2、获得嵌入输出
    embed = tf.nn.embedding_lookup(params=lookup_w, ids=input_data)
    # [N, n_steps, embed_size]
    return embed


# todo 使用函数[`tf.nn.dynamic_rnn()`]创建RNN
"""
- 使用函数[`tf.nn.dynamic_rnn()`]创建RNN。
- 对final state应用[`tf.identity()`]，并命名为："final_state"（name='final_state'）
Return :a tuple `(Outputs, FinalState)` 
"""


def build_rnn(cell, inputs, initial_state):
    """
    Create a RNN using a RNN Cell
    :param cell: RNN Cell
    :param inputs: 传入嵌入的输出（而不是Input占位符）
    :return: Tuple (Outputs, Final State)
    """
    # todo：
    rnn_outputs, final_state = tf.nn.dynamic_rnn(
        cell, inputs, initial_state=initial_state
    )
    # rnn_outputs shape = [批量， 时间步， 隐藏层节点数量]

    final_state1 = tf.identity(final_state, name='final_state')
    return rnn_outputs, final_state, final_state1


# todo 构建RNN网络
"""
运用上面完成的函数，完成以下应用：
- 将输入：`input_data`传入函数 `get_embed(input_data, vocab_size, embed_dim)` 并获得嵌入输出。
- 使用`cell` 和函数 `build_rnn(cell, inputs)`构建RNN；
- 应用一个全连接层（使用线性激活），输出节点个数== `vocab_size` 。
Return：a tuple (Logits, FinalState) 
"""


def build_nn(cell, input_data, vocab_size, embed_dim, initial_state):
    """
    Build part of the neural network
    :param cell: RNN cell
    :param rnn_size: Size of rnns
    :param input_data: Input data
    :param vocab_size: Vocabulary size
    :param embed_dim: Number of embedding dimensions
    :return: Tuple (Logits, FinalState)
    """
    # todo 1、获取嵌入层的输出
    embed = get_embed(input_data, vocab_size, embed_dim)
    # todo-2、获取 隐藏层的输出
    rnn_outputs, final_state, final_state1 = build_rnn(
        cell, embed, initial_state=initial_state)
    # 3、构建全连接，获取logits
    # 该api接受3-d 的张量，会拉成2-d矩阵，做全连接获得2-d的logits后，再转置为3-D的logits（shape = [批量， 时间步， 类别数量]）
    logits = tf.contrib.layers.fully_connected(rnn_outputs, vocab_size, activation_fn=None)
    # [N, n-steps, num_classes]
    return logits, final_state, final_state1


# todo 批次
"""
完成`get_batches`函数的代码编写：使用 `int_text`创建input 和 targets的batches。 The batches是一个 Numpy数组， 
shape =`(number of batches, 2, batch size, sequence length)`。每一个batch包含2部分:
- 第一部分是单个**input**的batch,  shape = `[batch size, sequence length]`
- 第二部分是单个**targets**的batch, shape = `[batch size, sequence length]`
最后一个batch没有办法填充满，那么就直接丢弃掉。

例如： `get_batches([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 2, 3)` 返回以下形式的Numpy数组:
[
  # First Batch
  [
    # Batch of Input
    [[ 1  2  3], [ 7  8  9]],
    # Batch of targets
    [[ 2  3  4], [ 8  9 10]]
  ],

  # Second Batch
  [
    # Batch of Input
    [[ 4  5  6], [10 11 12]],
    # Batch of targets
    [[ 5  6  7], [11 12 13]]
  ]
]
"""


# todo-方法一
def get_batches(int_text, batch_size, n_steps):
    """
    Return batches of input and target
    :param int_text: Text with the words replaced by their ids
    :param batch_size: The size of batch
    :param n_steps: The length of sequence
    :return: Batches as a Numpy array
    """
    # todo 需要编程：
    # 计算有多少个批量
    n_batches = len(int_text) // (batch_size * n_steps)

    origin_x = np.array(int_text[:n_batches * batch_size * n_steps])
    origin_y = np.array(int_text[1: n_batches * batch_size * n_steps + 1])

    # 对origin重塑
    x_reshaped = np.reshape(origin_x, newshape=[batch_size, -1])
    y_reshaped = np.reshape(origin_y, newshape=[batch_size, -1])

    batch_reshape_x = np.split(x_reshaped, n_batches, axis=1)
    batch_reshape_y = np.split(y_reshaped, n_batches, axis=1)

    batches = np.array(list(zip(batch_reshape_x, batch_reshape_y)))
    return batches


# todo 超参数的设置
num_epochs = 80  # 训练次数
batch_size = 32  # 批量大小
rnn_size = 128  # RNN隐藏层节点数量大小（神经元个数）
embed_dim = 200  # 嵌入维度大小 Embedding Dimension Size
seq_length = 100  # 序列长度（就是 n_steps）
learning_rate = 1e-3
show_every_n_batches = 30  # 打印进度的批次数量
save_dir = './save'

# todo 构建模型图（损失和 优化器在模型图中构建。）
train_graph = tf.Graph()
with train_graph.as_default():
    vocab_size = len(int_to_vocab)
    input_text, targets, lr, keep_prob = get_inputs()
    input_data_shape = tf.shape(input_text)
    multi_cell, initial_state, initial_state1 = get_init_cell(
        input_data_shape[0], rnn_size, keep_prob)
    logits, final_state, final_state1 = build_nn(
        multi_cell, input_text, vocab_size, embed_dim, initial_state)

    # 生成单词的概率
    probs = tf.nn.softmax(logits, name='probs')

    # 损失函数 Loss function
    """
    将交叉熵损失的函数过程全部封装在该函数内了。（average_across_timesteps average_across_batch 
                             两个参数使用True的情况下，返回一个标量loss(即该批次的均交叉熵损失。)）
    seq2seq.sequence_loss(
      logits,           # [batch_size, sequence_length, num_decoder_symbols]
      targets,          # [batch_size, sequence_length] 使用的是真实标签，所以是2-D的。
      weights,          # [batch_size, sequence_length] 作为掩码（比如有效的时间步为1，padding的设置为0）  
      average_across_timesteps=True,  # 设置为True的话，会沿着 时间步 累加loss并求均值。
      average_across_batch=True,      # 设置为True的话，会沿着 批次 累加loss并求均值。
      softmax_loss_function=None,
      name=None):
    """
    cost = seq2seq.sequence_loss(
        logits=logits, targets=targets,
        weights=tf.ones([input_data_shape[0], input_data_shape[1]])
    )

    optimizer = tf.train.AdamOptimizer(lr)

    # 梯度裁剪
    gradients = optimizer.compute_gradients(cost)
    capped_gradients = [(tf.clip_by_value(grad, -1., 1.), var) for grad, var in gradients if grad is not None]
    train_op = optimizer.apply_gradients(capped_gradients)


# todo 训练
def training():
    batches = get_batches(int_text, batch_size, seq_length)
    with tf.Session(graph=train_graph) as sess:
        sess.run(tf.global_variables_initializer())

        for epoch_i in range(num_epochs):
            # 将initial_state 跑出来，并赋值给state。
            state = sess.run(initial_state, {input_text: batches[0][0]})

            for batch_i, (x, y) in enumerate(batches):
                feed = {input_text: x, targets: y, initial_state: state,
                        lr: learning_rate, keep_prob: 0.6}
                train_loss, state, _ = sess.run([cost, final_state, train_op], feed)

                # 每30步 打印1次模型损失。
                if (epoch_i * len(batches) + batch_i) % show_every_n_batches == 0:
                    print('Epoch {:>3} Batch {:>4}/{}   train_loss = {:.3f}'.format(
                        epoch_i,
                        batch_i,
                        len(batches),
                        train_loss))

        # 模型持久化
        saver = tf.train.Saver()
        saver.save(sess, save_dir)
        print('Model Trained and Saved')


# Save parameters for checkpoint
helper.save_params((seq_length, save_dir))


# todo 生成电视剧本

# checkpoints
_, vocab_to_int, int_to_vocab, token_dict = helper.load_preprocess()
seq_length, load_dir = helper.load_params()

"""
### Get Tensors
使用函数[`get_tensor_by_name()`](https://www.tensorflow.org/api_docs/python/tf/Graph#get_tensor_by_name)中的方法`loaded_graph`获取tensors。Tensors中的名字如下：
- "input:0"
- "initial_state:0"
- "final_state:0"
- "probs:0"
Return：a tuple `(InputTensor, InitialStateTensor, FinalStateTensor, ProbsTensor)`
"""


def get_tensors(loaded_graph):
    """
    Get input, initial state, final state, and probabilities tensor from <loaded_graph>
    :param loaded_graph: TensorFlow graph loaded from file
    :return: Tuple (InputTensor, InitialStateTensor, FinalStateTensor, ProbsTensor)
    """
    # todo 需要编程：
    input_tensor = loaded_graph.get_tensor_by_name('input:0')
    keep_prob = loaded_graph.get_tensor_by_name('keep_prob:0')
    initial_state_tensor = loaded_graph.get_tensor_by_name("initial_state:0")
    final_state_tensor = loaded_graph.get_tensor_by_name("final_state:0")
    probs_tensor = loaded_graph.get_tensor_by_name("probs:0")
    return input_tensor, initial_state_tensor, final_state_tensor, probs_tensor, keep_prob


# Choose Word
#   使用 `probabilities`参数选取下一个次（选取概率最大的单词）
def pick_word(probabilities, int_to_vocab):
    """
    Pick the next word in the generated text
    :param probabilities: Probabilites of the next word
    :param int_to_vocab: Dictionary of word ids as the keys and words as the values
    :return: String of the predicted word
    """
    # todo 需要编程：
    word = int_to_vocab[np.argmax(probabilities)]
    return word


# todo 使用训练模型生成电视剧本
def test():
    gen_length = 200
    # homer_simpson, moe_szyslak, or Barney_Gumble
    prime_word = 'homer_simpson'
    # print(vocab_to_int)
    # print(vocab_to_int[prime_word])

    loaded_graph = tf.Graph()
    with tf.Session(graph=loaded_graph) as sess:
        # 载入保存的模型
        loader = tf.train.import_meta_graph(load_dir + '.meta')
        loader.restore(sess, load_dir)

        # 从载入的模型获取 tensors
        input_text, initial_state, final_state, probs, keep_prob = get_tensors(loaded_graph)

        # 句子生成设置
        gen_sentences = [prime_word + ':']
        prev_state = sess.run(initial_state, {input_text: np.array([[1]])})

        # 生成句子
        for n in range(gen_length):
            # 动态输入
            dyn_input = [[vocab_to_int[word] for word in gen_sentences[-seq_length:]]]
            # print(dyn_input)
            dyn_seq_length = len(dyn_input[0])

            # 获取预测值
            probabilities, prev_state = sess.run(
                [probs, final_state],
                {input_text: dyn_input, initial_state: prev_state, keep_prob: 1.0})

            pred_word = pick_word(probabilities[0][dyn_seq_length - 1], int_to_vocab)

            gen_sentences.append(pred_word)

        # 将标点符号 切换回来。
        tv_script = ' '.join(gen_sentences)
        for key, token in token_dict.items():
            ending = ' ' if key in ['\n', '(', '"'] else ''
            tv_script = tv_script.replace(' ' + token.lower(), key)
        tv_script = tv_script.replace('\n ', '\n')
        tv_script = tv_script.replace('( ', '(')

        print(tv_script)


if __name__ == '__main__':
    # preprocess_and_save_data()
    # training()
    test()
