# Parking-Lot-detection

![Lenna](https://user-images.githubusercontent.com/79725511/109583232-90228d80-7acd-11eb-806a-118bddef05b6.jpg)

![ParkingLot](https://user-images.githubusercontent.com/79725511/109583233-90bb2400-7acd-11eb-82f5-02d0fa0ddb7a.jpg)

> A quick snap of the orginal Lenna image and the parking lot image.
> Lenna or Lena is a standard test image widely used in the field of image processing since 1973. It is a picture of the Swedish model Lena Forsén, shot by photographer Dwight Hooker, cropped from the centerfold of the November 1972 issue of Playboy magazine.

---

### Table of Contents

- [Description](#description)
- [Technologies](#technologies)
- [License](#license)
- [Author Info](#author-info)

---

## Description

Implemented image processing techniques on the popular Lenna image and on a parking lot image. Some of the basic operations include RGB to gray conversion, down sampling the image from 256 * 256 to 64 * 64, edge detection using Convolution technique, histogram analysis, cumulative histogram analysis, histogram equalizaton, comparing the difference between the original image and the histogram equalized image, Parking lane lines detection using hough transform, polar transform, and finding the parking spot using the detected lane lines.

The final output of the above said operations: 

1) RGB to Gray image

![RGB2Gray_Lenna](https://user-images.githubusercontent.com/79725511/109581609-96633a80-7aca-11eb-9598-25bfd737e73f.png)

2) Down sampling from 256 * 256 to 64 * 64

![DownSampling_Lenna](https://user-images.githubusercontent.com/79725511/109581602-95caa400-7aca-11eb-904f-747c466515ce.png)

3) Edge detection using convolution

![Convolution_edges_Lenna](https://user-images.githubusercontent.com/79725511/109581599-95320d80-7aca-11eb-8b5f-be5ed92f01de.png)

4) Histogram analysis

![Histogram_Lenna_Gray](https://user-images.githubusercontent.com/79725511/109581606-96633a80-7aca-11eb-94a2-6c4e28bb962e.png)

5) Cumulative histogram analysis

![Cumulative_histogram_Lenna_Gray](https://user-images.githubusercontent.com/79725511/109581601-95caa400-7aca-11eb-82d5-40f15f9e83b1.png)

6) Histogram equalization

![Histogram_Equalized_Lenna_Gray](https://user-images.githubusercontent.com/79725511/109581605-95caa400-7aca-11eb-8903-02d992c0062f.png)

7) Difference between the original and the equalized image

![Equalized_image_Lenna](https://user-images.githubusercontent.com/79725511/109581603-95caa400-7aca-11eb-9393-520f2cae89ea.png)

8) Histogram analysis of parking lot image

![Histogram_Parking_Lot](https://user-images.githubusercontent.com/79725511/109581607-96633a80-7aca-11eb-8528-606378c0830b.png)

9) Binary image conversion

![Binary_image_parkinglot](https://user-images.githubusercontent.com/79725511/109581598-95320d80-7aca-11eb-89ab-a813e3cf68f0.png) 

10) Parking lane detection using hough transform

![parking_lines](https://user-images.githubusercontent.com/79725511/109581504-65830580-7aca-11eb-8aed-9bb35aca99c7.png)

11) Polar transform

![Polar_transform_parkinglot](https://user-images.githubusercontent.com/79725511/109581608-96633a80-7aca-11eb-9433-b63217fb65d1.png)

12) Parking spot detection using the detected line points

![Parking_spot](https://user-images.githubusercontent.com/79725511/109581505-65830580-7aca-11eb-8126-cbedb4d6737e.png)


## Technologies

- Python
- OpenCV
- Visual studio code
- Colaboratory

[Back To The Top](#Parking-Lot-detection)

---

## License

MIT License

Copyright (c) [2021] [Venkat Narayanan Balachandran]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#Parking-Lot-detection)

---

## Author Info

- LinkedIn - [Venkat_Narayanan_Balachandran](https://www.linkedin.com/in/venkat-balachandran)

[Back To The Top](#Parking-Lot-detection)

