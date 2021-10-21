# Searchings-and-Sortings
<h2>Searching Techniques</h2>
<h4>Definations</h4>
<ul>
  <li>The process of finding the desired information from the set of items stored in the form of elements in the computer memory is referred to as ‘searching in data structure’.</li>
  <li>Searching is an operation or a technique that helps finds the place of a given element or value in the list</li>
</ul>
<h3>Types of Searching Techniques</h3>
<ol>
  <li>Linear Search</li>
  <li>Binary Search</li>
</ol>
<h3>Linear Search</h3>
<p>Linear search is a very basic and simple search algorithm. <br>
In Linear search, we search an element or value in a given array by traversing the array from the starting, till the desired element or value is found.</p>
<h3>Algorithm</h3>
<ol>
  <li>Take an array and the search key. Assume they are:- array and key</li>
  <li>Traverse through the array.</li>
  <li>Compare key with each element</li>
  <li>If the match is found then return the position</li>
  <li>Else repeat the process until the end of the array</li>
  <li>After traversing the array If the match is not found then return -1</li>
</ol>
<h3>Binary Search</h3>
<p>Binary Search is applied on the sorted array or list of large size</p>
<h3>Algorithm</h3>
<ul>
  <li> Start with the middle element</li>
  <ul>
    <li>If the target value is equal to the middle element of the array, then return the index of the middle element</li>
    <li>If not, then compare the middle element with the target value,</li>
    <ul>
      <li>If the target value is greater than the number in the middle index, then pick the elements to the right of the middle index, and start with Step 1</li>
      <li>If the target value is less than the number in the middle index, then pick the elements to the left of the middle index, and start with Step 1.</li>
    </ul>
  </ul>
  <li>When a match is found, return the index of the element matched.</li>
  <li>If no match is found, then return target value is not found</li>
</ul>
<h2>Sorting Techniques</h2>
<ul>
  <li>Sorting is nothing but arranging the data in ascending or descending order.</li>
  <li>Sorting arranges data in a sequence which makes searching easier.</li>
</ul>
