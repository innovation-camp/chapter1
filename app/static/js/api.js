export default async function api(url,method,data){
    const response = await fetch(url,{
        method:method,
        mode:'cors',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    })

    return response.json()
}
