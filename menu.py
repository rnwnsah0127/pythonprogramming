from Library import Library

def print_menu():
    print('\n' + '='*40)
    print('   📚 도서 관리 시스템')
    print('='*40)
    print('1.도서추가  2.전체조회  3.검색')
    print('4.회원등록  5.대출      6.반납')
    print('0. 종료')
    print('-'*40)

def menu_add_book(library):
    title = input("도서명:").strip()
    author = input("저자:").strip()
    isbn = input("ISBN:").strip()
    
    try:
        total_copies = int(input("권 수 입력: ").strip())
    except ValueError:
        print("권 수는 숫자로 입력해주세요.")
        return
    library.add_book(title,author,isbn,total_copies)

def menu_search(library):
    keyword = input("검색어:").strip()

    print("1. 제목 검색")
    print("2. 저자 검색")

    choice = input("검색.").strip()

    if choice == 1:
        library.search_books(keyword,"title")
    elif choice == 2:
        library.search_books(keyword,"author")
    else:
        print("잘못된 선택입니다.")
def menu_register_member(library):
    member_id = input("회원 번호 : ").strip()
    name = input("이름 : ").strip()
    phone = input("전화번호 : ").strip()

    library.register_member(member_id,name,phone)
    print("회원 등록이 완료되었습니다")

def menu_borrow(library):
    pass
def menu_return(library):
    pass