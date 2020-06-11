<template>
	<view>
	<view>{{msg}}</view>
	<view class="box" v-for="item in list">
		{{item}}
	</view>
	<!-- <button @click="showmsg()" type="default">click</button>	 -->
	</view>
</template>

<script>
	export default{
		data(){
			return{
				msg:"内容",
				list:["js","java","bigdata","vue","js","java","bigdata","vue"]
			}
		}, 
		onPullDownRefresh() {
			setTimeout(()=>{
				this.list=["js","vue"]
				uni.stopPullDownRefresh()	
			},2000)

		},
		methods:{
			showmsg(){
				this.msg="点击时内容",
				uni.startPullDownRefresh({
					
				})
			}
		},
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		},
		onBackPress(options) {
			console.log('from:' + options.from)
		}
	}
</script>

<style>
	.box{
		height: 100px;
		line-height: 200px;
	}
</style>
