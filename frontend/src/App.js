import React, { useState } from "react";
import Register from "./components/Register";
import PasswordList from "./components/PasswordList";

function App() {
  const [userId, setUserId] = useState(1); // Temporary static user ID

  return (
    <div>
      <h1>Secure Password Manager</h1>
      <Register />
      <PasswordList userId={userId} />
    </div>
  );
}

export default App;
