// An Axios interceptor
// Checks if we have an access token and it'll automatically add it to the request

import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

const apiUrl = "/choreo-apis/djangoreacttutorial/backend/v1"

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl,  // Import anything thats specified in .env (Anything imported must start with VITE)
});

api.interceptors.request.use(
    // Looks in local storage to see if we have ACCESS_TOKEN. If we do it'll add it to the auth header to the request
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`; //  Header must be "Bearer {token}. `` to pass string in string."
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;