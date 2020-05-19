// pages/mapManager/mapManager.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    markers: [{
      id: 1,
      latitude: 22.540822,
      longitude: 113.934457,
      name: '腾讯大厦',
      label: {
        content: '这是腾讯大厦',
        color: '#333',
        x: 4,
        y: 0,
        borderWidth: 1,
        borderRadius:5,
        borderColor: '#000',
        bgColor: '#fff',
        padding: 2,
        textAlign: 'center'
      }
    },
    {
      id: 2,
      latitude: 39.892778,
      longitude: 116.421915,
      name: '北京',
      callout: {
        centent: '这是祖国首都',
        color: '#fff',
        fontSize: 16,
        borderRadius: 10,
        bgColor: '#000',
        display: 'ALWAYS'
      }
    }]
  },

  onReady: function(e) {
    // 获取map上下文
    this.mapCtx = wx.createMapContext('idMap')
  },

  getCenterLocation: function() {
    this.mapCtx.getCenterLocation({
      success: function(res){
        console.log(res.longitude)
        console.log(res.latitude)
      }
    })
  },

  moveToLocation: function() {
    this.mapCtx.moveToLocation()
  },

  translateMarker: function(){
    this.mapCtx.translateMarker({
      markerId: 1,
      autuRotate: true,
      duration: 1000,
      destination: {
        latitude: 22.940822,
        longitude: 113.934457,
      },
      animationEnd() {
        console.log('animation End')
      }
    })
  },
  includePoints: function(){
    this.mapCtx.includePoints({
      padding: [10],
      points: [{
        latitude: 22.540822,
        longitude: 113.934457,
      },{
        latitude: 22.840822,
        longitude: 114.234457, 
      }]
    })
  },

  getRegion: function(){
    this.mapCtx.getRegion({
      success: function(res){
        console.log('当前视野范围信息', res)
      }
    })
  },

  getScale: function(){
    this.mapCtx.getScale({
      success: function(res){
        console.log('当前缩放级别',res)
      }
    })
  }
})