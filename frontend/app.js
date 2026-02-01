const API_BASE = "http://127.0.0.1:8000/api";

function login() {
  axios.post(`${API_BASE}/accounts/login/`, {
    username: document.getElementById("username").value,
    password: document.getElementById("password").value
  }).then(res => {
    localStorage.setItem("access", res.data.access);
    alert("Login successful");
    window.location.href = "dashboard.html";
  }).catch(err => {
    alert("Login failed");
  });
}

function authHeader() {
  return {
    headers: {
      Authorization: "Bearer " + localStorage.getItem("access")
    }
  };
}
