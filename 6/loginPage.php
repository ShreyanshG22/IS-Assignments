<?php
	include("config.php");
   	if( $_GET["username"] || $_GET["pasword"] ) {
      		$sql = "SELECT id FROM users WHERE username = '".$_GET['username']."' and password = '".$_GET['password']."'";
      		$result = mysqli_query($db,$sql);
      		$row = mysqli_fetch_array($result,MYSQLI_ASSOC);
      		$active = $row['active'];
      		$count = mysqli_num_rows($result);
        	if($count == 1) {
         		echo "Welcome ". $_GET['username']. "<br/>";
      			echo "Password ". $_GET['password'];
      		}else {
         		$error = "Your Login Name or Password is invalid";
			echo $error;
      		}
      		exit();
   	}
?>
<html>
   
   <head>
      <title>Login Page</title>
      
      <style type = "text/css">
         body {
            font-family:Arial, Helvetica, sans-serif;
            font-size:14px;
         }
         label {
            font-weight:bold;
            width:100px;
            font-size:14px;
         }
         .box {
            border:#666666 solid 1px;
         }
      </style>
      
   </head>
   
   <body bgcolor = "#FFFFFF">
	
      <div align = "center">
         <div style = "width:300px; border: solid 1px #333333; " align = "left">
            <div style = "background-color:#333333; color:#FFFFFF; padding:3px;"><b>Login</b></div>
				
            <div style = "margin:30px">
               
               <form action = "" method = "GET">
                  <label>UserName  :</label><input type="text" name = "username"/><br /><br />
                  <label>Password  :</label><input type="password" name = "password"  /><br/><br />
                  <input type = "submit" value = " Submit "/><br />
               </form>
               
               <div style = "font-size:11px; color:#cc0000; margin-top:10px"><?php echo $error; ?></div>
					
            </div>
				
         </div>
			
      </div>

   </body>
</html>
