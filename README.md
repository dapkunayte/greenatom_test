<h2>1. Какие шаги ты бы предпринял, если бы пользователь сказал, что API возвращает ему ошибку 500?</h2>
<p>Хотелось бы рассмотреть два случая по обработке такой ситуации.</p>
<h3>Ситуация 1. Поддержка API осуществляется одним человеком</h3>
Последовательность шагов:
<ol>
<li>Уточнить у пользователя, какой запрос и какие данные в запросе вызывают ошибку</li>
<li>На основании ответа пользователя проверить часть кода, которая отвечает за обработку запроса</li>
<li>Исправить проблему, из-за которой возникала ошибка (это может быть как некорректная работа реализованной логики, так и не обработанные альтернативные сценарии работы</li>
<li>Оповестить клиента (а лучше всех клиентов), что вышла новая версия API, в котором исправлены ошибки</li>
</ol>
<h3>Ситуация 2. Поддержка API осуществляется несколькими людьми</h3>
<ol>
<li>Специалист тех.поддержки фиксирует обращение пользователя с проблемой</li>
<li>Тестировщик воспроизводит дефект (повторяет шаги пользователя, приведшие к ошибке)</li>
<li>В случае воспроизведения дефекта он оформляется в баг-трекере, после чего его необходимо обработать</li>
<li>Далее (в зависимости от причин возникновения дефекта, может быть недоработка аналитики или проблема в реализации) Аналитик и/или разработчик исправляют причину возникновения дефекта</li>
<li>Клиенты оповещаются о выходе новой версии с исправлением дефектов</li>
</ol>
<h2>2. Какие проблемы в фрагменте кода?</h2>
<p> Пояснения и исправление кода представлены в файле task_2_(problem_solving)</p>
<h2>3. Сколько HTML-тегов в коде главной страницы сайта greenatom.ru?</h2>
<p>Для выполнения этого задания потребуется установка зависимостей (использовал библиотеку beautifulsoup)</p>
<h4>Установка (прописать в терминале):</h4>
<ul>
<li>pip install poetry</li>
<li>poetry install</li>
</ul>
<p> Скрипт на python приведен в файле task_3_(html_tags)</p>
<h2>4. Функция на Python, которая возвращает текущий публичный ip-адрес</h2>
<p> Скрипт на python приведен в файле task_4_(return_ip)</p>
<h2>5. Функция на Python, выполняющая сравнение версий</h2>
<p> Скрипт на python приведен в файле task_5_(version_comparison)</p>