# major_change
Creates a Sankey diagram using Google Charts of major/school change sequence codes

# description
In order to track movement between colleges at a private university, students' enrollment over the course of 6 semesters was coded into a 1-6 letter sequence. In the example of code 'PPRBBB,' a student started at college P, remained there for the second semester, switched to college R in their third semester, then moved to college B and remained there for the following three semesters.

<a href="https://en.wikipedia.org/wiki/Sankey_diagram">Sankey diagrams</a> were chosen to capture this movement. Using <a href="http://www.stonybrook.edu/commcms/irpe/reports/presentations/VisualizationSankey_Hoffman_2015_05_30.pdf"> Sean V. Hoffman's</a> work as a jumping-off point, a Python script was written to convert the sequence into nodes and weights to be used with <a href="https://developers.google.com/chart/interactive/docs/gallery/sankey">Google Charts.</a>


Original intention was to translate this to JavaScript, thus the "python" folder, but this idea was scrapped (for the time being).
