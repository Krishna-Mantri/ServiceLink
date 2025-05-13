// document.addEventListener("DOMContentLoaded", function() {
//     if (document.getElementById("workers-container")) {
//         loadWorkers();
//     }
//     if (document.getElementById("bookings-container")) {
//         loadBookings();
//     }
//     if (document.getElementById("worker-name")) {
//         loadWorkerProfile();
//     }
// });

// // Load workers dynamically
// function loadWorkers() {
//     fetch("http://127.0.0.1:8000/api/workers/")
//         .then(response => response.json())
//         .then(data => {
//             let workersContainer = document.getElementById("workers-container");
//             workersContainer.innerHTML = "";

//             data.forEach(worker => {
//                 let workerCard = document.createElement("div");
//                 workerCard.className = "worker-card";
//                 workerCard.innerHTML = `
//                     <div>
//                         <h3>${worker.user}</h3>
//                         <p>${worker.job_type} | ${worker.location}</p>
//                         <p>₹${worker.hourly_rate} per hour</p>
//                     </div>
//                     <button onclick="viewWorker(${worker.id})">View</button>
//                 `;
//                 workersContainer.appendChild(workerCard);
//             });
//         });
// }

// function viewWorker(workerId) {
//     window.location.href = `worker_profile.html?id=${workerId}`;
// }

// function loadWorkerProfile() {
//     let params = new URLSearchParams(window.location.search);
//     let workerId = params.get("id");

//     fetch(`http://127.0.0.1:8000/api/workers/${workerId}/`)
//         .then(response => response.json())
//         .then(worker => {
//             document.getElementById("worker-name").textContent = worker.user;
//             document.getElementById("worker-job").textContent = worker.job_type;
//             document.getElementById("worker-experience").textContent = worker.experience;
//             document.getElementById("worker-rate").textContent = worker.hourly_rate;
//             document.getElementById("worker-location").textContent = worker.location;
//             document.getElementById("worker-availability").textContent = worker.is_available ? "Available" : "Not Available";
//         });
// }

// function bookWorker() {
//     alert("Booking functionality coming soon!");
// }

// function loadBookings() {
//     fetch("http://127.0.0.1:8000/api/bookings/")
//         .then(response => response.json())
//         .then(data => {
//             let container = document.getElementById("bookings-container");
//             container.innerHTML = "";

//             data.forEach(booking => {
//                 container.innerHTML += `<tr>
//                     <td>${booking.worker}</td>
//                     <td>${booking.date_time}</td>
//                     <td>${booking.duration}</td>
//                     <td>₹${booking.total_cost}</td>
//                     <td>${booking.status}</td>
//                 </tr>`;
//             });
//         });
// }



document.addEventListener("DOMContentLoaded", function() {
    console.log("City Service Link UI Loaded");
});