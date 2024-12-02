'use client';

const GETUSERURL = 'http://localhost:5000/services/user/';
const GETURL = 'http://localhost:5000/services/';
const POSTURL = 'http://localhost:5000/services/create';
const DELETEURL = 'http://localhost:5000/services/delete/';

export async function getUserServices(user_id) {
    try {
        const apiURL = GETUSERURL + user_id;
        const response = await fetch(apiURL, { method: 'GET' });

        if (!response.ok) {
             new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // If the data is a single service
        if (Array.isArray(data) && data.length === 6) {
            // Return the single service in the desired format
            return [{
                id: data[0],
                title: data[1],
                content: data[2],
                price: data[3],
                created_at: data[4],
                user_id: data[5],
            }];
        }

        // If the data is an array of services
        if (Array.isArray(data) && data.length > 0) {
            return data.map((servicedata) => ({
                id: servicedata[0],
                title: servicedata[1],
                content: servicedata[2],
                price: servicedata[3],
                created_at: servicedata[4],
                user_id: servicedata[5],
            }));
        }

        // If no services are returned, return an empty array
        return [];
    } catch (error) {
        console.error('Error fetching user services:', error);
        return [];  // Return an empty array in case of an error
    }
}


export async function getService(service_id) {
    try{
        const apiURL = GETURL+ service_id;
        const response = await fetch(apiURL,{method: 'GET'});
        if(!response.ok){
            new Error(`HTTP error! status: ${response.status}`);
        }
        const servicedata = await response.json();
        const service ={
            id: servicedata[0],
            title:servicedata[1],
            content:servicedata[2],
            price:servicedata[3],
            created_at:servicedata[4],
            user_id:servicedata[5],
        }
        return await response.json();
    }catch(error){
        console.error(error);
    }
}

export async function updateService(service_id,data) {
    try{
        const apiURL = 'http://localhost:5000/services/update'+service_id;
        const response = await fetch(apiURL,{
            method: 'PUT',
            headers: {'Content-Type': 'application/json',},
            body:JSON.stringify(data)});
        if(!response.ok){
            new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }catch(error){
    console.error(error);
}
}
export async function createService(user_id,data){
    try{
        const response = await fetch(POSTURL,{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body:JSON.stringify(data)
        });
        console.log(JSON.stringify(data))
        if(!response.ok){
            new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }catch(error){
        console.error(error);
    }
}

export async function deleteService(service_id){
    try{
        const apiURL = DELETEURL+ service_id;
        const response = await fetch(apiURL,{method: 'DELETE'});
        if(!response.ok){
            new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }catch(error){
        console.error(error);
    }
}
