import React, { useEffect, useState } from "react";
import { getPasswords } from "../api";

const PasswordList = ({ userId }) => {
  const [passwords, setPasswords] = useState([]);

  useEffect(() => {
    const fetchPasswords = async () => {
      try {
        const response = await getPasswords(userId);
        setPasswords(response.data);
      } catch (error) {
        alert("Error fetching passwords.");
      }
    };
    fetchPasswords();
  }, [userId]);

  return (
    <div>
      <h2>Stored Passwords</h2>
      <ul>
        {passwords.map((p, index) => (
          <li key={index}>
            {p.website} - {p.username} - {p.password}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PasswordList;
