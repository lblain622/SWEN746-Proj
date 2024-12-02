'use client';

const url = 'http://localhost:5000/profile'
export async function getProfile(user_id) {
    try{
        const apiURL = 'http://localhost:5000/profile/'+user_id;
        const response = await fetch(apiURL,{method: 'GET'});

        if(!response.ok){
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const profiledata = await response.json();
        return {
            id: profiledata[0],
            first_name: profiledata[1],
            last_name: profiledata[2],
            age: profiledata[3],
            sex: profiledata[4],
            student_id: profiledata[5],
        }
    }catch(err){
        console.error(err);
        throw err;
    }
}

export async function updateProfile(profile_id,form_data){
    try{
        const apiURL = 'http://localhost:5000/profile/'+profile_id;
        const response = await fetch(apiURL,{
            method: 'PUT',
            headers: {'Content-Type': 'application/json',},
            body:JSON.stringify(form_data)});
        if(!response.ok){
           new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();

    }catch(err){
    console.error(err);
    throw err;
    }
}

