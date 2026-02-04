"use client";
import { useEffect,useState } from "react";
import { whoAmI,logout } from "../lib/api";

export default function Dashboard(){
    const[user,setUser]=useState(null);
    useEffect(()=>{
        async function loadUser(){
            const data=await whoAmI();
            if(!data||data.user===null){
                window.location.href="/";
                return;
            }
            setUser(data);
        }
        loadUser();
    },[]);
const handleLogout=async()=>{
    await logout();
    window.location.href="/";
};
if(!user) return <p>Loading...</p>;
return(
    <div style={{padding:40}}>
        <h1>Dashboard</h1>
        <p>Welcome {user.username}</p>
        <button onClick={handleLogout}>
            Logout
        </button>
    </div>
);
}