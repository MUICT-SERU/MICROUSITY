let onlineTestApp = new function () {

    this.printPage = function () {
 // Import dependencies
 const fs = require("fs");
 const moment = require("moment");
 const PDFDocument = require("pdfkit");

 // Create the PDF document
 const doc = new PDFDocument({
   layout: "landscape",
   size: "A4",
 });

 // The name
 const name = "Sophia Sweet"

 // Pipe the PDF into an name.pdf file
 doc.pipe(fs.createWriteStream(`${name}.pdf`));

 // Draw the certificate image
 doc.image("public/Pic/certificate.PNG", 0, 0, { width: 842 });

 // Draw the name
 doc.fontSize(60).text(name, 90, 320, {
   align: "center"
 });

 // Draw the date
 doc.fontSize(15).text(moment().format("MMMM Do YYYY"), 175, 420, {
   align: "center"
 });

 // Finalize the PDF and end the stream
 doc.end();
}
}
