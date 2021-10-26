def Manchester_Encode(signal):
    print('Manchester Encoding')
    for s in signal:
        if s=='1':print('[low to high transition]',end=' ')
        else :print('[high to low transition]',end=' ')


def Differential_Manchester_Encode(signal):
    print('Differential Manchester Encoding')
    initsignal = 0  # 시그널을 0과 1로 표현 초기 시그널 = 0
    l = []
    for s in signal:
        if s=='1':
            initsignal = 1 - initsignal
            print('[signal transition]',end=' ')
        else:
            print('[no transition]',end=' ')
        l.append(initsignal)
    print()
    print(l)



if __name__ == '__main__':
    signal = '0100110100'

    print('--------------------SIGNAL--------------------------')
    print(signal)
    print('----------------------------------------------------')
    Manchester_Encode(signal)

    print()
    print('----------------------------------------------------')
    Differential_Manchester_Encode(signal)