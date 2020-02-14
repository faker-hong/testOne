Page({

  onReady: function (res) {
    this.videoContext = wx.createVideoContext('myVideo')
  },

  inputValue: '',

  data: {
    src: '',
    danmuList: [
      {
      text: '第1S出现的弹幕',
      color: '#ff0000',
      time: 1
      },
      {
        text: '第3S出现的弹幕',
        color: '#ff00ff',
        time: 3
      }

    ],
  },
  
  bindInputBlur: function(e){
    this.inputValue = e.detail.value
  },

  bindSendDanmu: function(e) {
    this.videoContext.sendDanmu({
      text: this.inputValue,
      color: 'red'
    })
  }

})