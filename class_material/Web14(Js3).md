### Event

- 개념

  - 네트워크 활동이나 사용자와의 상호작용 같은 사거느이 발생을 알리기 위한 객체
  - 이벤트 발생
    - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
    - 특정 메서드를 호출하여(Element.click())하여 프로그래밍적으로도 만들어 낼 수 있다

- Event 역할

  - ~하면 ~ 한다. 
  - 클릭하면 경고창을 띄운다. 
  - 특정 이벤트가 발생하면, 할 일(함수)을 등록한다.

- Event handler - addEventListener() 

  - EventTarget.addEventListener()(1/4)
    - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
    - 이벤트를 지원하는 모든 객체(Elment, Document, window 등)를 대상으로 지정 가능

  

  - target.addEventListener(type, listener[, options])

    - type

      - 반응 할 이벤트 유형 (대소문자 구분 문자열)

    - listener

      - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
      - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 한다.

      

  - addEventListener() (4/4) 

    - 대상에 특정 이벤트가 발생하면, 할 일을 등록하자

    

  

  

  

- Event 취소
  - event.preventDefault()
  - 현재 이벤트의 기본 동작을 중단
  - HTML 요소의 기본 동작을 작동하지 않게 막음
    - ex) a 태그의 기본 동작은 클릭 시 링크로 이동/ form 태그의 기본 동작은 form 데이터 전송
  - 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소
  - 취소 할 수 없는 이벤트도 존재
    - 이벤트의 취소 가능 여부는 event.cancelable을 사용해 확인할 수 있다.
- Event 추가 학습
  - 다양한 이벤트 유형 참고
  - https://developer.mozilla.org/en-US/docs/Web/Events