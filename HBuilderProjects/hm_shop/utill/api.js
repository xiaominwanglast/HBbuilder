const BASE_URL="https://www.fastmock.site/mock/ac6ecc367950e9507b26ce210b97a5a9";
export const myRequest =(options) =>{
	return new Promise((resolve,reject)=>{
		uni.request({
			url:BASE_URL+options.url,
			method:options.method || "GET",
			data:options.data || {},
			success:(res)=> {
				if(res.data.status!=0){
					return uni.showToast({
						title:"获取数据失败"
					})
				}
				resolve(res)
			},
			fail:(err)=>{
				return uni.showToast({
					title:"接口异常"
				}),
				reject(err)
			}
		})
	}
	)
}