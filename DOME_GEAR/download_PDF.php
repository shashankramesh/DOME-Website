<?php  
sleep(1);
 function fetch_data($table = "PDF")  
 {  
      $servername = "localhost";
      $username = "root";
      $password = "";
      $dbname = "mydatabase";

      $output = '';  
      $conn = mysqli_connect($servername, $username, $password, $dbname);  
      $sql = "SELECT * FROM $table ORDER BY id ASC";  
      $Result = mysqli_query($conn, $sql);  
      while($row = mysqli_fetch_array($Result))  
      {       
      $output .= '<tr>  
                          <td>'.$row["id"].'</td>  
                          <td>'.$row["Name"].'</td> 
                          <td>'.$row["Value"].'</td>    
                  </tr>
                          ';  
      }  
      return $output;  
 }  
 // if(isset($_POST["Gen_pdf"]))  
 // {  
      require_once('tcpdf/tcpdf.php');  
      $obj_pdf = new TCPDF('P', PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);  
      $obj_pdf->SetCreator(PDF_CREATOR);  
      $obj_pdf->SetTitle("Factor of Safety parameters");  
      $obj_pdf->SetHeaderData('', '', PDF_HEADER_TITLE, PDF_HEADER_STRING);  
      $obj_pdf->setHeaderFont(Array(PDF_FONT_NAME_MAIN, '', PDF_FONT_SIZE_MAIN));  
      $obj_pdf->setFooterFont(Array(PDF_FONT_NAME_DATA, '', PDF_FONT_SIZE_DATA));  
      $obj_pdf->SetDefaultMonospacedFont('helvetica');  
      $obj_pdf->SetFooterMargin(PDF_MARGIN_FOOTER);  
      $obj_pdf->SetMargins(PDF_MARGIN_LEFT, '10', PDF_MARGIN_RIGHT);  
      $obj_pdf->setPrintHeader(false);  
      $obj_pdf->setPrintFooter(TRUE);  
      $obj_pdf->SetAutoPageBreak(TRUE, 10);  
      $obj_pdf->SetFont('helvetica', '', 11);  
      $obj_pdf->AddPage();  
      $content = '';  
      $content .= '  
      <h4 align="center">Factor of Safety</h4><br /> 
      <table border="1" cellspacing="0" cellpadding="3" align = "center">  
           <tr>  
                <th width="5%">Id</th>  
                <th width="30%">Name</th>  
                <th width="30%">Value</th>
           </tr>  
      ';  
      $content .= fetch_data("FOS");  
      $content .= '</table>';  
      $content .= '  
      <h4 align="center">Other Safety parameters</h4><br /> 
      <table border="1" cellspacing="0" cellpadding="5" align = "center">  
           <tr>  
                <th width="5%">Id</th>  
                <th width="30%">Name</th>  
                <th width="30%">Value</th>
           </tr>  
      ';  
      $content .= fetch_data();   // FOS table
      $content .= '</table>';      
      $content .= '
      <footer>
      <p>copyright @ iii & Shank </p>
      </footer>';
      
      $obj_pdf->writeHTML($content);  
      $obj_pdf->Output('file.pdf', 'I');  
 // }  
 ?> 
<!--
  <!DOCTYPE html>  
 <html>  
      <head>  
           <title>SoftAOX | Generate HTML Table Data To PDF From MySQL Database Using TCPDF In PHP</title>  
           <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />            
      </head>  
      <body>  
           <br />
           <div class="container">  
                <h4 align="center"> Generate HTML Table Data To PDF From MySQL Database Using TCPDF In PHP</h4><br />  
                <div class="table-responsive">  
                  <div class="col-md-12" align="right">
                     <form method="post">  
                          <input type="submit" name="generate_pdf" class="btn btn-success" value="Generate PDF" />  
                     </form>  
                     </div>
                     <br/>
                     <br/>
                     <table class="table table-bordered">  
                          <tr>  
                               <th width="5%">Id</th>  
                               <th width="30%">Bending</th>  
                          </tr>  
                     <?php  
                     //echo fetch_data();  
                     ?>  
                     </table>  
                </div>  
           </div>  
      </body>  
</html>
-->