import axios from "axios"
import pbkdf2 from "crypto-js/pbkdf2"


const serverUrl = 'http://localhost:8080/';

export function encrypt(password){
    let encrypted = pbkdf2(password, 'secret');
    console.log(encrypted.toString())
    return encrypted.toString();
}

export function get_auth_key_server(username, password){

    return axios.post(serverUrl+"auth", {password: password, username: username})
        .then(res => {
            if(!res.data.token){
                localStorage.setItem("auth_token", "");
            }else{
                console.log(res.data.token)
                localStorage.setItem("auth_token", res.data.token);
                localStorage.setItem("user_name", res.data.username)
            }


        }).catch(err => {
            localStorage.setItem("auth_token", "");
        });
}

export function get_restricted(){
    console.log(localStorage.getItem("auth_token"))
    return axios.get(serverUrl+"secret_page", {
        headers: {token: localStorage.getItem("auth_token")}
    }).then(res => res.data)
}

export function user_has_auth_key(){
    let token = localStorage.getItem("auth_token");
    if(token){
        return token;
    }
    return "No token set"

}
