import React, { useState } from "react";
import { registerUser } from "../api";

const Register = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {
    try {
      await registerUser({ username, password });
      alert("User Registered!");
    } catch (error) {
      alert("Error registering user.");
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
};

export default Register;
