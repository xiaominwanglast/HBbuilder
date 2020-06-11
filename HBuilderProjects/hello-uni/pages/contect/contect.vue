<template>
	<view>
		<button type="primary" @click="upphotos">上传</button>
		<image v-for="item in imageArr" :src="item" @click="previewImage(item)"></image>
	</view>
</template>

<script>
	export default{
		data(){
			return{
				imageArr:[]
			}
		},
		methods:{
			upphotos(){
				uni.chooseImage({
					count:5,
					success:res=> {
						console.log(res)
						this.imageArr=res.tempFilePaths
						console.log(this.imageArr)
					}
				})
			},
			previewImage(current){
				console.log(current),
				uni.previewImage({
					current:current,
					urls:this.imageArr,
					indicator:"number"
				})
			}
		}
	}
</script>

<style>
</style>
