<?php
	ini_set('max_execution_time', 0);
	require '../connect.inc.php';
?>

<!DOCTYPE html>
<html>
<head>
	<title>Pehchaan : Confirmation</title>
		<!-- Latest compiled and minified CSS -->
	 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
 	
<!-- custom style -->
	<link rel="stylesheet" type="text/css" href="fetch.css">
</head>
<body style="background-color: rgba(12, 151, 244, 0.08)">


	<nav class="navbar navbar-default ultra-nav navbar-fixed-top">

	  <div class="container">
	    <div class="navbar-header">
	      <!-- <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar"> -->
	        <span class="icon-bar"></span>
	        <span class="icon-bar"></span>
	        <span class="icon-bar"></span>                        
	      </button>
	      <a class="navbar-brand make-white" href="../">Pehchaan</a>
	    </div>
	   <!--  <div class="collapse navbar-collapse" id="myNavbar">
	      <ul class="nav navbar-nav navbar-right">
	        <li><a data-scroll class="make-white" href="#about">About</a></li>
	        <li><a data-scroll class="make-white" href="#teams">Our Teams</a></li>
	        <li><a data-scroll  class="make-white"  href="#activities">Our Activities</a></li>
	        <li><a data-scroll  class="make-white" href="#contact">Contact</a></li>
	      </ul>
	    </div> -->
	  </div>
	</nav>

	<div class="container  main" style="margin-top: 10%; text-align: center;">		
		<h3>Attendance Report<br></h3>
		<table class="table table-striped" >
		  <tr>
		    <!-- <th>Photo</th> -->
		    <th style="text-align: center;">Name</th> 
		    <th style="text-align: center;">Enrollment Number</th>
		    <th style="text-align: center;">Accuracy</th>
		    <th style="text-align: center;">Attendance</th>
		  </tr>

	<?php
		
		$query = 'SELECT * FROM `students` WHERE 1';
		if ($result = mysqli_query($con, $query)) {
			while ($row = mysqli_fetch_assoc($result)) {
				$output = exec('python fetch_data.py '. $row['roll_no']);
				$parsed = json_decode($output, True);
				// print_r($parsed);
				// if($parsed['roll_number'] != $row['roll_no']){


	?>

		  <tr>
		    <!-- <td><img src=""></td> -->
		    <td><?php echo $row['name'];?></td> 
		    <td><?php echo $row['roll_no'];?></td>
		    <td><?php echo $parsed['confidence'];?></td>
		    <td><input type="checkbox" name="present" <?php if (!empty($parsed['confidence'])) {
		    	echo 'checked';
		    }?>></td>
		  </tr>

	<?php
				// }
			}
		}else echo mysqli_error($con);
		  

	?><!-- 
		  <tr>
		    <td><img src=""></td>
		    <td>Jackson</td> 
		    <td>05915603115</td>
		    <td><input type="checkbox" name="present"></td>
		  </tr> -->
		</table>
		<button type="button" id="done" class="btn btn-info">Done</button>
	</div>




</body>
<script type="text/javascript">
	
	document.getElementById("done").addEventListener("click", function(){

		window.location.href = "index.php";

	});



</script>
</html>
