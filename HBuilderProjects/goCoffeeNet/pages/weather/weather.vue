<template>
	<view>
		<web-view :src="url"></web-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				url:"http://wx.weather.com.cn"
			}
		},
		methods: {
			
		},
		onNavigationBarButtonTap:function(e){
			console.log(e)
		},
		onLoad:function(){
			uni.navigateTo({
				url:this.url
			})
		}
	}
</script>

<style>

</style>
