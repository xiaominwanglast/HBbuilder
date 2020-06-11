<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
	@font-face {font-family: "iconfont";
	  src: url('https://gitee.com/destiny001/iconfont/iconfont.eot?t=1586060239063'); /* IE9 */
	  src: url('https://gitee.com/destiny001/iconfont/iconfont.eot?t=1586060239063#iefix') format('embedded-opentype'), /* IE6-IE8 */
	  url('data:application/x-font-woff2;charset=utf-8;base64,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') format('woff2'),
	  url('https://gitee.com/destiny001/iconfont/iconfont.woff?t=1586060239063') format('woff'),
	  url('https://gitee.com/destiny001/iconfont/iconfont.ttf?t=1586060239063') format('truetype'), /* chrome, firefox, opera, Safari, Android, iOS 4.2+ */
	  url('https://gitee.com/destiny001/iconfont/iconfont.svg?t=1586060239063#iconfont') format('svg'); /* iOS 4.1- */
	}
	
	.iconfont {
	  font-family: "iconfont" !important;
	  font-size: 16px;
	  font-style: normal;
	  -webkit-font-smoothing: antialiased;
	  -moz-osx-font-smoothing: grayscale;
	}
	
	.icon-bofang:before {
	  content: "\e681";
	}
	
	.icon-tupian:before {
	  content: "\e630";
	}
	
	.icon-CONTACT:before {
	  content: "\e601";
	}
	
	.icon-fuwuchaoshi:before {
	  content: "\e61c";
	}
	
	.icon-ren:before {
	  content: "\e647";
	}
	
	.icon-ren-copy:before {
	  content: "\e648";
	}
	
	.icon-wangluo:before {
	  content: "\e62f";
	}
	
	.icon-wangluo-copy:before {
	  content: "\e641";
	}
	
	.icon-gouwuche:before {
	  content: "\e632";
	}
	
	.icon-gouwuche-copy:before {
	  content: "\e640";
	}
	
	.icon-shouye:before {
	  content: "\e63e";
	}
	
	.icon-shouye-copy:before {
	  content: "\e63f";
	}
</style>
