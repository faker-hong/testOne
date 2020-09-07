Page({

  /**
   * 页面的初始数据
   */
  data: {
    
  },

  toastTap: function () {
    wx.showToast({
      title: 'toast',
      duration: 5000, //持续时间
      icon: 'loading',  //3中状态，success，loading，none
    })
  },

  modalTap: function() {
    wx.showModal({
      title: 'Modal',
      content: '今天是否打球',
      success: function(res){
        console.log(res)
      }
    })
  },

  actionSheetTap: function(){
    wx.showActionSheet({
      itemList: ['a', 'b', 'c', 'd'],
      success: function(e) {
        console.log(e)
      },
      fail: function(e){
        console.log(e, '取消')
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  }
})