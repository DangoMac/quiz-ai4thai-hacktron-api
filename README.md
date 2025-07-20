# Quiz-ai4thai-hacktron-api

Russian Roulette API (FastAPI + Docker Compose)
โปรเจกต์นี้จำลองเกม Russian Roulette ด้วย API 2 ตัว ที่เชื่อมต่อกันด้วย HTTP  
- API1 รับคำขอจากผู้ใช้
- API1 ส่งคำขอไปยัง API2 เพื่อสุ่มผลลัพธ์
- API2 เป็นตัวตัดสินว่า "ตาย" หรือ "ไม่ตาย" (สุ่มตัวเลข 1 ถึง 6 ถ้าได้ 1 "ตาย")

## วิธี Deploy ด้วย Docker Compose

## วิธีใช้งาน API
### ใช้งานผ่าน Swagger UI (Interactive API Docs)
1. เปิดเบราว์เซอร์ไปที่: http://localhost:8000/docs
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6a8b9064-f283-4bb4-994d-8ded68f55771" />


2. เลือก endpoint /api1
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f66abceb-99b4-443c-8e30-61a1c976206b" />


3. กดปุ่ม "Try it out" แล้วใส่ชื่อในช่อง player
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d9033ec6-88d9-4a52-af34-cdecd08a4e50" />


4. คลิก "Execute"
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c014d632-b2fc-4210-8470-444d1932f408" />


5. ดูผลลัพธ์ที่แสดงด้านล่าง พร้อมสถานะ HTTP Response (เช่น 200 OK)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2b6b8d57-aa38-45fa-9095-563d11e70ac9" />


### Log แสดงผลผ่าน Terminal
<img width="1528" height="475" alt="image" src="https://github.com/user-attachments/assets/db7d6d4e-f39f-43c9-bcb1-a7b0150c8907" />


### ใช้งานผ่าน Postman
1. เปิด Postman แล้วสร้าง Request ใหม่
2. กำหนด Method เป็น GET
3. URL เป็น http://localhost:8000/api1?player=Jirasak
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ebfdca94-415a-4565-a2be-d11560dabe97" />


4. กดปุ่ม Send และดูผลลัพธ์ในส่วน Response
<img width="1922" height="1080" alt="image" src="https://github.com/user-attachments/assets/92e485c8-5f4d-46b0-a166-785f5052db50" />

### Log แสดงผลผ่าน Terminal
<img width="1530" height="442" alt="image" src="https://github.com/user-attachments/assets/208ae20e-2db6-46d3-8860-5b6175c346f0" />



