import axios from "axios";

const API_URL = "http://localhost:5000";

export const registerUser = (user) => axios.post(`${API_URL}/register`, user);
export const storePassword = (passwordData) => axios.post(`${API_URL}/store-password`, passwordData);
export const getPasswords = (userId) => axios.get(`${API_URL}/get-passwords/${userId}`);
