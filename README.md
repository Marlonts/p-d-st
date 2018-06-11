### Java jdk
Update repository

	$ sudo add-apt-repository ppa:openjdk-r/ppa
	$ sudo apt-get update

Run the following command in Terminal:

	$ sudo apt-get install openjdk-8-jdk
	$ sudo apt-get install openjdk-8-source #this is optional, the jdk source code

Type commandline as below...

	$ apt-cache search jdk
(Note: openjdk-8-jdk is symbolically used here. You can choose the JDK version as per your requirement.)

For "JAVA_HOME" (Environment Variable) type command as shown below, in "Terminal" using your installation path...

	$ export JAVA_HOME=/usr/lib/jvm/java-8-openjdk
(Note: "/usr/lib/jvm/java-8-openjdk" is symbolically used here just for demostration. You should use your path as per your installation.)

For "PATH" (Environment Variable) type command as shown below, in "Terminal" using your installation path...

	$ export PATH=$PATH:/usr/lib/jvm/java-8-openjdk/bin
(Note: "/usr/lib/jvm/java-8-openjdk" is symbolically used here just for demostration. You should use your path as per your installation.)

Check for "open jdk" installation, just type command in "Terminal" as shown below

	$ javac -version

### pip
	$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	$ sudo python get-pip.py

### Apache
	$ sudo apt-get install apache2
	$ sudo pip install pyspark

http://localhost:4040/

http://localhost:4040/jobs/


-----------------------------------------------------------------------------------------------

### Download Spark

	http://spark.apache.org/downloads.html

		http://ftp.unicamp.br/pub/apache/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz 

### Pyspark
	$ sudo pip install pyspark

### Interactive Analysis with the Spark Shell
	$ ./bin/spark-shell
ou

	$ pyspark

-----------------------------------------------------------------------------------------------

### Spark
https://pt.linkedin.com/pulse/machine-learning-com-apache-spark-uma-introdu%C3%A7%C3%A3o-%C3%A0-de-teixeira-phd
https://www.datacamp.com/community/tutorials/apache-spark-python
https://spark.apache.org/docs/latest/quick-start.html

https://www.devmedia.com.br/apache-spark-trabalhando-com-sql-em-aplicacoes-big-data/34251
http://www.vitormeriat.com.br/2016/01/27/spark-alm-do-wordcount/
https://docs.microsoft.com/en-us/azure/hdinsight/spark/apache-spark-machine-learning-mllib-ipython
https://www.infoq.com/br/articles/apache-spark-introduction

### Spark examples
https://spark.apache.org/examples.html
https://github.com/apache/spark/tree/master/examples

### Pyspark + Elastic Search
https://github.com/TargetHolding/pyspark-elastic
https://starsift.com/2018/01/18/integrating-pyspark-and-elasticsearch/
https://qbox.io/blog/elasticsearch-in-apache-spark-python?utm_source=qbox.io&utm_medium=article&utm_campaign=elasticsearch-in-apache-spark-python

### Apache Spark Streaming Tutorial: Identificando as Hashtags de Tendência do Twitter 
http://gtezini.blogspot.com/2017/07/apache-spark-streaming-tutorial.html

-----------------------------------------------------------------------------------------------

### Principais características:
    O Spark é escrito na linguagem Scala e executa em uma máquina virtual Java (JVM).
    Processamento rápido – todo o processamento em geral é feito em memória, e com reduzido processamento em disco, o que o torna muito mais rápido e eficiente.
    Expande de maneira mais eficiente a capacidade de processamento de operações Map+Reduce.
    Permite o processamento e tratamento de dados usando linguagem SQL, através da biblioteca SparkSQL.
    Permite processamento em “tempo real” em streaming, com a biblioteca Spark Streaming.
    Possibilita trabalhar com grafos com a biblioteca GraphX.
    Realiza processamento de análises complexas (machine learning) através da biblioteca MLlib.

	Em resumo, o Spark possui 4 bibliotecas principais: SparkSQL, Streaming, GraphX e a biblioteca de Machine Learning, MLlib.
	Além da linguagem Scala que é a linguagem “nativa”, o Spark também dispõe de APIs para outras 3 linguagens de programação: Python, R e Java. A figura abaixo mostra os principais componentes do Spark.
	O Spark pode ser usado na sua máquina local, em modo Standalone, que é o ideal para aprender a usar, ou pode instalá-lo para uso em um cluster, para efetivamente trabalhar em processamento distribuído. N

-----------------------------------------------------------------------------------------------

### Exemplos de operações de transformação:
	• map (func) - retorna um novo RDD aplicando a função func em
	cada elemento.
	• filter (func) - retorn um novo RDD aplicando o filtro func.
	• flatMap (func) - similar ao map, mas retornando mais itens ao invés
	de apenas um.
	• sample(withReplacement, fração, semente) - amostra aleatoriamente
	uma fração dos dados com ou sem reposição usando a semente para
	gerar os números aleatórios.
	• union(rdd) - retorna um novo RDD que contém a união dos ele-
	mentos do RDD original e do RDD passado como argumento.
	• distinct() - retorna um novo dataset contendo os valores distintos
	do RDD original.
	• groupByKey() - aplicado em pair RDD’s da forma (K, V), retor-
	nando um novo pair RDD da forma (K, iterable<V>).
	• reduceByKey(func) - aplicado também em um pair RDD (K, V),
	agregando os valores de V pela função func para cada chave K.
	• pipe(command) - aplica para cada partição do RDD um comando
	shell. Qualquer linguagem com stdin, stdout pode ser utilizada.
	Algumas operações de ação são:
	• collect() - retorna todos os elementos do RDD como um array para
	o driver. Usado principalmente após uma operação de filtro para
	retornar poucos dados.
	• count() - retorno o número de elementos no RDD.
	• first() - retorna o primeiro elemento do dataset.
	• take(n) - retorna os primeiros n elementos do dataset.
	• saveAsTextFile(file) - salva o RDD em um arquivo de texto
