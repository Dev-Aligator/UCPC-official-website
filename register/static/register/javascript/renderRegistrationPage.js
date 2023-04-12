// document.querySelector(".registration_btn").addEventListener("click", function () {
//     let deadline = "May 2, 2022 15:27:00"
//     let countDown = new Date(deadline).getTime()
//     let now = new Date().getTime()
//     let distance = countDown - now
//     if (distance < 0) {
//         const html = notallowRegister()
//         const registrationPage = document.querySelector(".registration_page")
//         if (registrationPage) {
//             console.log("het thoi gian dang ky")
//             registrationPage.innerHTML = html;
//         }
//     } else {
//         const html = allowRegister()
//         const registrationPage = document.querySelector(".registration_page")
//         if (registrationPage) {
//             console.log("con thoi gian dang ky")
//             registrationPage.innerHTML = html;
//         }
//     }
// })

// function notallowRegister() {
//     return `
//         <div class="container" style="margin-top: 15px;">
//             <h3>Đã hết  thời gian đăng ký!</h3>
//         </div>
        
//         <hr>
//     `
// }

// function allowRegister() {
//     return `
//         <div class="container" style="margin-top: 15px;">
//         <h3>Đăng ký</h3>
//         </div>

//         <hr>

//         {% for message in messages %}
//         <p id="messages">{{message}}</p>
//         {% endfor %}

//         <div class="form-group">
//             <div class="container">
//                 <!-- <form id="registration_form" action="{% url 'register:register' %}" method="POST"> -->
//                 <form id="registration_form" method="POST">
//                     {% csrf_token %}

//                     {{ tf.team.label }}<br>
//                     {{ tf.team }}
//                     <small>{{ tf.team.errors }}</small><br>

//                     {{ tf.member1.label }}<br>
//                     {{ tf.member1 }}
//                     <small>{{ tf.member1.errors }}</small>
//                     {{ tf.cmnd1.label }}<br>
//                     {{ tf.cmnd1 }}
//                     <small>{{ tf.cmnd1.errors }}</small>
//                     {{ tf.phone1.label }}<br>
//                     {{ tf.phone1 }}
//                     <small>{{ tf.phone1.errors }}</small>
//                     {{ tf.school1.label }}<br>
//                     {{ tf.school1 }}
//                     <datalist id="schools">
//                         <option>Trường Đại học Công nghệ Thông tin - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Bách khoa - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Khoa học Tự nhiên - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Quốc Tế - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Khoa học Xã hội và Nhân văn - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Sư phạm Kỹ thuật Thành phố Hồ Chí Minh</option>
//                         <option>Học viện Công nghệ Bưu Chính Viễn thông</option>
//                         <option>Trường Đại học Sư Phạm Thành phố Hồ Chí Minh</option>
//                         <option>Trường Đại học Công nghiệp Thành phố Hồ Chí Minh</option>
//                         <option>Trường Đại học Thủ Dầu Một</option>
//                         <option>Trường Trung học phổ thông Gia Định</option>
//                     </datalist>	
//                     <small>{{ tf.school1.errors }}</small><br>

//                     {{ tf.member2.label }}<br>
//                     {{ tf.member2 }}
//                     <small>{{ tf.member2.errors }}</small>
//                     {{ tf.cmnd2.label }}<br>
//                     {{ tf.cmnd2 }}
//                     <small>{{ tf.cmnd2.errors }}</small>
//                     {{ tf.phone2.label }}<br>
//                     {{ tf.phone2 }}
//                     <small>{{ tf.phone2.errors }}</small>
//                     {{ tf.school2.label }}<br>
//                     {{ tf.school2 }}
//                     <datalist id="schools">
//                         <option>Trường Đại học Công nghệ Thông tin - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Bách khoa - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Khoa học Tự nhiên - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Quốc Tế - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Khoa học Xã hội và Nhân văn - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Sư phạm Kỹ thuật Thành phố Hồ Chí Minh</option>
//                         <option>Học viện Công nghệ Bưu Chính Viễn thông</option>
//                         <option>Trường Đại học Sư Phạm Thành phố Hồ Chí Minh</option>
//                         <option>Trường Đại học Công nghiệp Thành phố Hồ Chí Minh</option>
//                         <option>Trường Đại học Thủ Dầu Một</option>
//                         <option>Trường Trung học phổ thông Gia Định</option>
//                     </datalist>	
//                     <small>{{ tf.school2.errors }}</small><br>

//                     {{ tf.member3.label }}<br>
//                     {{ tf.member3 }}
//                     <small>{{ tf.member3.errors }}</small>
//                     {{ tf.cmnd3.label }}<br>
//                     {{ tf.cmnd3 }}
//                     <small>{{ tf.cmnd3.errors }}</small>
//                     {{ tf.phone3.label }}<br>
//                     {{ tf.phone3 }}
//                     <small>{{ tf.phone3.errors }}</small>
//                     {{ tf.school3.label }}<br>
//                     {{ tf.school3 }}
//                     <datalist id="schools">
//                         <option>Trường Đại học Công nghệ Thông tin - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Bách khoa - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Khoa học Tự nhiên - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Quốc Tế - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Khoa học Xã hội và Nhân văn - Đại học Quốc gia TP.HCM</option>
//                         <option>Trường Đại học Sư phạm Kỹ thuật Thành phố Hồ Chí Minh</option>
//                         <option>Học viện Công nghệ Bưu Chính Viễn thông</option>
//                         <option>Trường Đại học Sư Phạm Thành phố Hồ Chí Minh</option>
//                         <option>Trường Đại học Công nghiệp Thành phố Hồ Chí Minh</option>
//                         <option>Trường Đại học Thủ Dầu Một</option>
//                         <option>Trường Trung học phổ thông Gia Định</option>
//                     </datalist>	
//                     <small>{{ tf.school3.errors }}</small><br>

//                     {{ tf.email.label }}<br>
//                     {{ tf.email }}
//                     <small>{{ tf.email.errors }}</small>
//                     <p style="margin-top: 4px;">ℹ️ Email đăng ký được Ban Tổ Chức dùng để liên lạc với đội thi.</p>
//                     {{ tf.password.label }}<br>
//                     {{ tf.password }}
//                     <small>{{ tf.password.errors }}</small>
//                     <button type="submit" class="btn btn-primary" style="margin-top: 10px;">Đăng ký</button>
//                 </form>
//             </div>
//         </div>
//     `
// }



// // django => endTime =>