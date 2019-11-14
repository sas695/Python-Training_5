
<div class="rendered-markdown"><h1>Programming Assignment 5</h1>
<p><strong>Fundamentals of Modern Software</strong>
<br  /><strong>Fall 2019</strong>
<br  /><strong>Due 11:59 PM, Friday October 11</strong></p>
<h2>Introduction</h2>
<p><strong>REMINDERS</strong></p>
<ol>
<li><strong>When you are done, be sure to submit your work.</strong></li>
<li><strong>You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.</strong></li>
<li><strong>Be sure to test your programs thoroughly. We will.</strong></li>
<li><strong>Your output should match the output in the samples EXACTLY, to the letter.</strong></li>
</ol>
<p>This assignment may be submitted for full credit by 11:59 PM on Friday, October 11, or with a 20% late submission penalty by 11:59 PM on Sunday, October 13.</p>
<h2>zipcode-queries.py</h2>
<p>Using the basicdb package and the <code>geo.json</code> database, write the following functions. <strong>Your functions should never attempt to read <code>geo.json</code> or <code>geozipcodes.csv</code> directly. All access to the data must be through the functions defined in <code>basicdb.py</code>.</strong></p>
<p><code>state_of(zipcode)</code>: Returns the name of the state in which <code>zipcode</code> is located.</p>
<p><code>northernmost(state)</code>: Returns the northernmost zipcode in <code>state</code>.</p>
<p><code>zipcodes_in_city(city_name)</code>: Returns the total number of zip codes in the City <code>city_name</code>.</p>
<p><code>states_by_size()</code>: Returns a list of state names, sorted in order from the state containing the fewest zip codes to the state containing the most. <em>This cannot be done solely using the basicdb interface. You will need to embed your calls to basicdb inside some additional Python code.</em></p>
<h2>classlist.py</h2>
<p>Using the basicdb package and the <code>registrar.json</code> database, write a program that takes a single command-line argument and prints out a report on a specified course:</p>
<pre><code>$ python classlistSOLUTION.py 3
Introduction to Asian History meets TH10 in Lecture Hall A
Albert Aziz
Derek Dortmund
Eustace Ennis
Frances Fan
Current enrollment: 4
Remaining capacity: 21
</code></pre>
<p><strong>Your program should never attempt to read the CSV files or the database schema directory. All access to the data must be through the functions defined in <code>basicdb.py</code>.</strong> You are welcome to use as many or as few queries as you like and to embed them in any additional Python code you wish.  Do <em>not</em> assume that the database contents are the same as in the sample files provided.  We will not change the schema, but we will test your program with a version of the database loaded with different or additional rooms, courses, and students.</p>
</div>
