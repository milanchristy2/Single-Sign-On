"use client";
import {login} from "../lib/api";
export default function Home(){
  return(
    <div style={{padding:40}}>
      <h1>SSO using GITHUB</h1>
      <button onClick={login}>
        Login with GITHUB
      </button>
    </div>
  );
}