#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:48:05 2021

@author: Alaisha Naidu
Name: HTML l7
Creds; Jen Simmons and CodePen
"""

<H3>Paragraphs</H3>

<p> To indicate a single paragraph, an opening p tag is used at the beginning of the 
text and then at the end of the paragraph, a closing p tag is used to close the paragraph like so </p>

<H3>Headlines </H3>

<H1> This is the largest and most pronounced headline </H1>
<H2> This is the second largest. Could be for subheadings </H2>
<H3> Headlines also require opening and closing tags </H3> 
<H4> There are six headline sizes </H4>
<H5> This is the second smallest headline font size </H3> 
<H6> This is the smallest headline font size </H6> 

<H3>Bold and Italics</H3>

  #italics
<em> tag is used to wrap something that should be verbally emphasized </em>
<i> tag is used to wrap the name of something, or something with no special meaning </i>

  #bold
<strong> element conveys importance and/or seriousness, conveys meaning </strong>
<b> element is a way of styling or marking something, no alternative mood </b> 

<H3>Lists</H3>

  #Undordered List 
<ul>
    <li> inidcates list item </li>
    <li> inidcated by bullets </li>
    <li> tab/space indentation is for human comprehension only </li>
</ul> 

  #Odered List
<ol>
    <li> inidcates list item </li>
    <li> inidcated by numbers </li>
    <li> tab/space indentation is for human comprehension only </li>    
</ol>

  #Definition List
<dl>
    <dt> Definition Term 1 </dt>
        <dd> definition description of term 1 </dd> 
        <dd> can have more than one defition for each term </dd> 
    <dt> Definition Term 2 </dt> 
        <dd> definition description of term 2 </dd>
    <dt> Definition Term 3 </dt> 
        <dd> definition description of term 3 </dd>
</dl>        
    

<H3>Quotes</H3>
    
    #Blockquote
<blockquote>
<p> The entire quote and the person who said it is wrapped in block tags 
where the p tags are used inside the block quote element to show what was said 
and the the author/person being quoted is cited at the end. </p> 

<cite> -Jen Simmons </cites>
</blockquote>

    #Inline
<p> Jen said, <q> the q element is an inline element which is wrapped around 
phrases of text. The q element changes depending on the lanuage to make the quote
grammatically correct. </q> </p> 


<H3>Dates and Time</H3>

    #Dates

<time> 8 May 2025 </time> 

<time datetime="2025-05-08">8 May 2025</time> 

## Machine readable format dor dates is YYYY-MM-DD

    #Time 
<time datetime="20:15 - 05:00">8:15pm in New York</time> 

## Machines wants a 24hr clock format for times hh-mm-ss.ddd+-hh:mm 
## where the +-hh:mm is the time difference from Grenwhich time 

    #Date and Time Together 
<time datetime="2020-11-04 19:00-05:00"> Wednesday 4 November 2020 at 7pm in New York</time>


<H3>Code, pre and br</H3> 
<p>
    #Code
    
<p> We can write <code>{colour:green;}</code> in our CSS, and it will apply to 
anything marked up as an <code>&lt;H4&gt;</code> element </p>

#&lt; < entity 
#&gt; > entity
</p>

    #br
<p>
This element gives us a way to <br>
break a line <br>
</p>
<cite> - Jen Simmons </cite>

    #pre
<pre> the <code>&lt;pre&gt;</code> tag
                keeps the 
irregular spacing 
            in a piece of text 
                just like it is typed 
so the browser pays attention 
        to the spacing and breaks in the text. 
 </pre>
 
 #pre and code are frequently combined to display a block of code in a browser<br>
 
 To show how to code a list in HTML on the browser use the following:<br>
 
<pre>
<code>
&lt;ul&gt;
    &lt;li&gt; item &lt;/li&gt;
    &lt;li&gt; item &lt;/li&gt;
    &lt;li&gt; item &lt;/li&gt;
&lt;/ul&gt; 
</code>
<pre> 
 
