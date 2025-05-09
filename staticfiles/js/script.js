document.getElementById('resultForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const studentId = document.getElementById('student_id').value;
    const resultDisplay = document.getElementById('resultDisplay');

    if (studentId.trim() === "") {
        resultDisplay.innerHTML = "الرجاء إدخال رقم الطالب.";
        return;
    }

    fetch(`http://127.0.0.1:8000/api/students/get-result/?student_id=${studentId}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                resultDisplay.innerHTML = `نتيجة الطالب: ${data.result}`;
            } else {
                resultDisplay.innerHTML = "لم يتم العثور على النتيجة.";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultDisplay.innerHTML = "حدث خطأ أثناء جلب البيانات.";
        });
});
