<template>
	<view class="goods-list">
		<goods-list 
		@goodsItemClick="goDetail" 
		:goods="goods"></goods-list>
		<view class="isOver" v-if="flag">---到底了---</view>
	</view>
</template>

<script>
	import goodslist from '../../components/goods-list/goods-list.vue'
	export default{
		data(){
			return{
				pageindex:1,
				goods:[],
				flag:false
			}
		},
		methods:{
			async getGoodsList(callback){
				const res=await this.$myRequest({
					url:"/api/lunbo/goods/"+this.pageindex
				})
				console.log(res)
				this.goods=[...this.goods,...res.data.message]
				callback && callback()
			},
			goDetail(id){
				// console.log("id",id) s
				uni.navigateTo({
					url:"/pages/goods-detail/goods-detail?id="+id
				})
			}
		},
		onLoad() {
			this.getGoodsList()
		},
		components:
		{
			"goods-list":goodslist
		},
		onReachBottom() {
			if (this.goods.length<this.pageindex*8) return this.flag=true
				this.pageindex++
				this.getGoodsList()	
			// console.log('到底了')

		},
		onPullDownRefresh() {
			console.log("下拉")
			this.pageindex=1
			this.flag=false
			setTimeout(()=>{
				this.getGoodsList(()=>{
					uni.stopPullDownRefresh()
				})
			},1000)
		}
	}

</script>

<style lang="scss">
	.goods-list{
		background-color: #eee;
		.isOver{
			width: 100%;
			text-align: center;
			height: 80rpx;
			line-height: 80rpx;
			// background-color: #C0C0C0;
		}
	}
</style>
