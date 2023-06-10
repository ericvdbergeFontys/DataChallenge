export const useProducts = async () => {
    let products = await $fetch('http://localhost:8000/products').catch((error) => error.data)
    products = products?.map(
        (v) => ({
            label: v.name,
            value: v.name
        })
    )
    return products
}