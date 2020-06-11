<template>
	<view>
		<web-view :src="url"></web-view>
	</view>
</template>

<script>
	export default{
		date(){
			return{
				url:""
			}
		},
		onLoad: function (option) { 
			this.url=option.url
		}
	}
</script>

<style>
</style>
