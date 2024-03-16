*** Settings ***
Library       Selenium2Library

*** Test Cases ***
Проверка валидных данных
    Open Browser   https://beregifiguru.ru/Калькуляторы/Расчет-размера-одежды    Chrome
    Click Button   xpath://*[@id="calcFormId"]/button
    Input Text   Height    160
    Input Text   Chest    90
    Input Text   Waist    60
    Input Text   Hips    90
    Click Button   xpath://*[@id="fieldsetForm"]/tbody/tr[9]/th/button
    Wait Until Page Contains   Ваш средний результат
    ${result_field} =   Get Text   xpath://*[@id="resvalueWrap"]/div
    Should Be Equal   44-46    ${result_field}
    Close Browser