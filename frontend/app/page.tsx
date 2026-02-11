"use client";
import {login} from "../services/api";
export default function Home(){
  return(
    <div style={{padding:40, textAlign:"center"}}>
      <button onClick={login}>
        <h1><b>Login with GITHUB</b></h1>
      </button>
    </div>
  );
}