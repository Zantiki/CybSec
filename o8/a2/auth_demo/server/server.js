const express = require("express")
const crypto = require("crypto-js")
let cors = require("cors");
let bodyParser = require("body-parser");
const jwt = require('jsonwebtoken');

const app = express();
app.use(cors({origin: true}));
app.use(bodyParser.json());

let tokens = [];
let publicKey = "secret";
let password = "68fed8e112277a3e27854f4e3a28fbac";

app.post("/auth", (req, res) => {

    let hash = crypto.PBKDF2(req.body.password, publicKey).toString()
    if(hash === password) {
        let token = jwt.sign({id: 'token'}, publicKey, {expiresIn: 10});
        tokens.push(token);
        setTimeout(() => {tokens.splice(tokens.indexOf(token), 1);}, 100)
        res.status(200).send({token: token, username: req.body.username});

    } else {
        res.sendStatus(403);
    }
})

app.get("/secret_page", (req, res) =>{

    console.log("Connected with token: "+req.headers.token);
    if(check_auth(req.headers.token)){
        console.log(check_auth(req.headers.token))
        res.send({data: "https://lumiere-a.akamaihd.net/v1/images/Yoda-Retina_2a7ecc26.jpeg?region=0%2C0%2C1536%2C864&width=960"})
    }else{
        res.send({data: "https://i2.wp.com/faithandlife.co.uk/wp-content/uploads/2018/03/access-denied.png?fit=750%2C496&ssl=1"})
    }
});

function check_auth(token){
    console.log(jwt.decode(token))
    return jwt.verify(token, publicKey, (err, decoded) => !err)



}
app.listen(8080);