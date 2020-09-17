import * as React from 'react';
import {Route, BrowserRouter} from 'react-router-dom';
import ReactDOM from 'react-dom';
import {createBrowserHistory} from "history";
import {Component, useState} from "react";
import {user_has_auth_key, get_auth_key_server, encrypt, get_restricted} from "./client";

const history = createBrowserHistory();

class Landing extends Component{

    state={
        password: "",
        username: "",
        token: "No tokens found",
        img: ""
    }

    constructor(props){
        super(props);
        this.handleUsername = this.handleUsername.bind(this);
        this.handlePwd = this.handlePwd.bind(this);
        this.get_token = this.get_token.bind(this);
        this.check_restricted = this.check_restricted.bind(this);
    }

    render(){
        return (
            <div>
                <h2>SECRET IMAGE VIEWER</h2>
                <h3>Input username and password</h3>
                <label>username</label>
                <input id="username" style={{marginLeft: "5px"}} onChange={this.handleUsername} type="text"></input>
                <label style={{marginLeft: "10px"}}>password</label>
                <input id="password" style={{marginLeft: "5px"}} onChange={this.handlePwd} type="password"></input>
                <button onClick={this.get_token}>Get auth-key</button>
                <p id="has_key">{this.state.token}</p>
                <button onClick={this.check_restricted}>Check your token</button>
                <div>
                    <img style={{marginTop: "20px"}} src={this.state.img}/>
                </div>
            </div>
        )
    }
    refresh(){
        this.render()
    }

    check_restricted(){
       return get_restricted()
            .then(res => this.setState({img: res.data}))

    }

    handlePwd(event){
        this.setState({password: event.target.value});
    }

    handleUsername(event){
        this.setState({username: event.target.value});
    }
    async get_token(){

        let hash = encrypt(this.state.password)

        await get_auth_key_server(this.state.username, hash)

        this.update_client_token()

    }
    update_client_token(){
        let auth_key = user_has_auth_key();
        this.setState({token: auth_key})

    }

    mounted(){
        this.update_client_token()
    }


}

const root = document.getElementById('root');
if (root) ReactDOM.render(
    <BrowserRouter history={history}>
        <Route exact path="/" component={Landing}/>
    </BrowserRouter>,
    root
);