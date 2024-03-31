*** Settings ***
Library       Selenium2Library

*** Keywords ***
Calculate
    [Arguments]    ${height}     ${chest}     ${waist}     ${hips}    ${result}
    Open Browser   https://beregifiguru.ru/Калькуляторы/Расчет-размера-одежды    Chrome
    Click Button   xpath://*[@id="calcFormId"]/button
    Input Text   Height    ${height}
    Input Text   Chest    ${chest}
    Input Text   Waist    ${waist}
    Input Text   Hips    ${hips}
    Click Button   xpath://*[@id="fieldsetForm"]/tbody/tr[9]/th/button
    Wait Until Page Contains   Ваш средний результат
    ${result_field} =   Get Text   xpath://*[@id="resvalueWrap"]/div
    Should Be Equal    ${result}    ${result_field}
    Close Browser

FailedCalculate
    [Arguments]    ${height}     ${chest}     ${waist}     ${hips}
    Open Browser   https://beregifiguru.ru/Калькуляторы/Расчет-размера-одежды    Chrome
    Click Button   xpath://*[@id="calcFormId"]/button
    Input Text   Height    ${height}
    Input Text   Chest    ${chest}
    Input Text   Waist    ${waist}
    Input Text   Hips    ${hips}
    Click Button   xpath://*[@id="fieldsetForm"]/tbody/tr[9]/th/button
    Page Should Contain    Введите значение
    Page Should not Contain    Ваш средний результат
    Close Browser



*** Test Cases ***
#Положительные тесты:

Валидные данные:
    Calculate    150    90    60    90    44-46

Ноль:
    Calculate    0    0    0    0    ${EMPTY}

Нулевой рост:
    Calculate    0    90    60    90    ${EMPTY}

Нулевой обхват груди:
    Calculate    150    0    60    90    ${EMPTY}

Нулевой обхват талии:
    Calculate    150    90    0    90    ${EMPTY}

Нулевой обхват бедер:
    Calculate    150    90    60    0    ${EMPTY}

Нереалистичные размеры:
    Calculate    20    20    20    20    ${EMPTY}

Дроби:
    Calculate    150,5    90,5    60,5    90,5    44-46

Единицы:
    Calculate    1    1    1    1    ${EMPTY}

Граничные значения - 1:
    Calculate    299    299    299    299    ${EMPTY}

Граничные значения:
    Calculate    300    300    300    300    ${EMPTY}

#Отрицательные тесты:

Граничные значения + 1:
    FailedCalculate    301    301    301    301

Отрицательные числа:
    FailedCalculate    -150    -90    -60    -90

Оставить поля пустыми:
    FailedCalculate    ${EMPTY}    ${EMPTY}    ${EMPTY}    ${EMPTY}

Не число:
    FailedCalculate    One    Two    Three    Four