import aspose.words as aw

# Load word document
doc = aw.Document("calibre.docx")

# Create save options and set image compression
saveOptions = aw.saving.PdfSaveOptions()
saveOptions.image_compression = aw.saving.PdfImageCompression.JPEG
saveOptions.jpeg_quality = 100 # Use JPEG compression at 50% quality to reduce file size.

# Save as PDF
doc.save("PDF.pdf", saveOptions)