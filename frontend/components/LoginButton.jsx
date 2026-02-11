"use client";
import { login } from "../services/api";

export default function LoginButton(){
    return (
        <button
            onClick={login}
            className="px-6 py-3 bg-black text-white rounded-lg"
        >
            Login 
        </button>
    );
}
