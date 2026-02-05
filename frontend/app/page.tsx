"use client";
import {login} from "../lib/api";
export default function Home(){
  return(
    <div style={{padding:40}}>
      <button onClick={login}>
        Login with GITHUB
      </button>
    </div>
  );
}