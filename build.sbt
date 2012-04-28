name := "onedit.py"

version := "0.1-SNAPSHOT"

scalaVersion := "2.9.2"

libraryDependencies += "org.python" % "jython-standalone" % "2.5.2"

managedClasspath in Runtime <+= (baseDirectory) map { bd => Attributed.blank(bd / "src/main/python") }
