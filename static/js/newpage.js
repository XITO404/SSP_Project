const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', ()=>{resvTab.classList.remove('open');
var listBody = document.getElementById('listBody');
while(listBody.hasChildNodes())
{
    listBody.removeChild(listBody.firstChild)
}});


// 날짜별로 이벤트 등록용 함수 및 변수
const selDate = []
const dateFunc = ()=>{
    const dates = document.querySelectorAll('.date');
    const year = document.querySelector('.year');
    const month = document.querySelector('.month');
    const tabYear = document.querySelector('.resv-year');
    const tabMonth = document.querySelector('.resv-month');
    const tabDay = document.querySelector('.resv-day');
    dates.forEach((i)=>{
        i.addEventListener('click', ()=>{
            if(i.classList.contains('other') || i.classList.contains('selected')){
                dates.forEach((ig)=>{ig.classList.remove('selected');});
                i.classList.remove('selected');
                selDate.length=0;
            }else if(selDate.length > 0){
                dates.forEach((ig)=>{ig.classList.remove('selected');});
                selDate.length=0;
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');
                tabYear.innerText = year.innerText;
                tabMonth.innerText = month.innerText;
                tabDay.innerText = i.innerText;
                var data = new FormData();
                var date = String(year.innerText + "-" + month.innerText + "-" + i.innerText)
                console.log(date)
                data.append('date', String(year.innerText + "-" + month.innerText + "-" + i.innerText))
                var responseData = null;
                console.log("insert start");
                async function Fetch()
                {
                    await fetch('/todoselect',{
                    method: 'post',
                    body: data,
                    })
                    .then((response)=>response.json())
                    .then((data)=> {
                        responseData = data
                    })
                    responseData.forEach((dataE) => {
                    console.log(dataE)
                    var tr = document.createElement("tr"); // 추가할 테이블 <tr> 생성
                    var input = document.createElement("input"); // 테이블 <tr> 안에 들어갈 체크박스의 <input> 생성
                    input.setAttribute("type", "checkbox"); // <input type="checkbox">
                    input.setAttribute("class", "btn-chk"); // <input type="checkbox" class="btn-chk">
                    input.setAttribute("id",dataE['content']);
                        input.addEventListener("change", checkTodo);
                    if (dataE['checked']) {
                        input.setAttribute("checked", "true");
                    }

                    var td01 = document.createElement("td"); // 첫 번째 <td> 생성 (체크박스를 담음)
                    td01.appendChild(input); // 첫 번째 <td> 안에 <input> 추가
                    var td02 = document.createElement("td"); // 두 번째 <td> 생성 (텍스트를 담음)
                    td02.innerHTML = dataE['content']; // 두 번째 <td> 안에 입력창의 텍스트를 저장
                    tr.appendChild(td01);
                    tr.appendChild(td02); // 생성된 <tr> 안에 체크박스 td와 텍스트 td를 넣음
                    document.getElementById("listBody").appendChild(tr); // tbody의 #listBody에 접근하여 tr을 자식요소로 추가
                    const button = document.createElement("button");
                    button.innerText="×";
                    button.addEventListener("click", deleteToDo);
                    tr.appendChild(button);
                    function deleteToDo(value) {
                      const tr=value.target.parentElement;
                      content = tr.firstChild.nextSibling.innerText
                        console.log(content)
                        var data = new FormData();
                        data.append('content', content)
                        tr.remove();
                        fetch('/tododelete',{
                            method: 'post',
                            body: data,
                            })
                        .then(function (response){
                            return console.log(response)
                        })
                    }
                     function checkTodo()
                    {
                        // const tr=value.target.parentElement;
                      content = this.id
                        var data = new FormData();
                        data.append('content', content)
                      fetch('/todocheck',{
                            method: 'post',
                            body: data,
                        })
                        .then(function (response){
                            return console.log(response)
                        })
                    }
                    })


                }
                Fetch()
            }else{
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');
                tabYear.innerText = year.innerText;
                tabMonth.innerText = month.innerText;
                tabDay.innerText = i.innerText;
                var data = new FormData();
                var date = String(year.innerText + "-" + month.innerText + "-" + i.innerText)
                console.log(date)
                data.append('date', String(year.innerText + "-" + month.innerText + "-" + i.innerText))
                var responseData = null;
                console.log("insert start");
                async function Fetch()
                {
                    await fetch('/todoselect',{
                    method: 'post',
                    body: data,
                    })
                    .then((response)=>response.json())
                    .then((data)=> {
                        responseData = data
                    })
                    responseData.forEach((dataE) => {
                    console.log(dataE)
                    var tr = document.createElement("tr"); // 추가할 테이블 <tr> 생성
                    var input = document.createElement("input"); // 테이블 <tr> 안에 들어갈 체크박스의 <input> 생성
                    input.setAttribute("type", "checkbox"); // <input type="checkbox">
                    input.setAttribute("class", "btn-chk"); // <input type="checkbox" class="btn-chk">
                    input.setAttribute("id",dataE['content']);
                        input.addEventListener("change", checkTodo);
                    if (dataE['checked']) {
                        input.setAttribute("checked", "true");
                    }

                    var td01 = document.createElement("td"); // 첫 번째 <td> 생성 (체크박스를 담음)
                    td01.appendChild(input); // 첫 번째 <td> 안에 <input> 추가
                    var td02 = document.createElement("td"); // 두 번째 <td> 생성 (텍스트를 담음)
                    td02.innerHTML = dataE['content']; // 두 번째 <td> 안에 입력창의 텍스트를 저장
                    tr.appendChild(td01);
                    tr.appendChild(td02); // 생성된 <tr> 안에 체크박스 td와 텍스트 td를 넣음
                    document.getElementById("listBody").appendChild(tr); // tbody의 #listBody에 접근하여 tr을 자식요소로 추가
                        const button = document.createElement("button");
                    button.innerText="×";
                    button.addEventListener("click", deleteToDo);
                    tr.appendChild(button);
                    function deleteToDo(value) {
                      const tr=value.target.parentElement;
                      content = tr.firstChild.nextSibling.innerText
                        var data = new FormData();
                        data.append('content', content)
                        tr.remove();
                        fetch('/tododelete',{
                            method: 'post',
                            body: data,
                            })
                        .then(function (response){
                            return console.log(response)
                        })
                    }
                    function checkTodo()
                    {
                        // const tr=value.target.parentElement;
                      content = this.id
                        var data = new FormData();
                        data.append('content', content)
                      fetch('/todocheck',{
                            method: 'post',
                            body: data,
                        })
                        .then(function (response){
                            return console.log(response)
                        })
                    }
                    })


                }
                Fetch()
            }
        });
    });
};

// 초기화 함수
const reset = ()=>{
    selDate.length=0;
    dateFunc();
}

// 로드시 Nav 버튼들 이벤트 등록 및 초기화
window.onload=()=>{
    const navBtn = document.querySelectorAll('.nav-btn');
    navBtn.forEach(inf=>{
        if(inf.classList.contains('go-prev')){
            inf.addEventListener('click', ()=>{prevMonth(); reset();});
        }else if(inf.classList.contains('go-today')){
            inf.addEventListener('click', ()=>{goToday(); reset();});
        }else if(inf.classList.contains('go-next')){
            inf.addEventListener('click', ()=>{nextMonth(); reset();});
        }
    });
    reset();
}


