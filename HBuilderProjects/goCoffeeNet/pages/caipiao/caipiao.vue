<template>
	<view>
		<web-view :src="url"></web-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				url:"https://m.jiangduoduo.com/home/nation"
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
