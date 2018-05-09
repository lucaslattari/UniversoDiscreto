/*criando um componente chamado Timer */
class Timer extends React.Component {
  /*atributos são adicionados aos componentes do react por meio dos props, estes
  podem ser usados para renderizar dados dinâmicos*/
  constructor(props){
    /*precisa invocar super, se não this.props fica indefinido no construtor, o que leva
    a bugs*/
    super(props);

    /*inicializamos o estado desse componente atribuindo um objeto com a propriedade currentTime
    com o valor 0*/
    this.state = {
      currentTime: 0
    }
  }

  /*função invocada continuamente para incrementar o relógio em uma unidade*/
  tick(){
    /*atualiza o estado atual do componente, tomando o cuidado de incrementar o valor
    antes de renderizá-lo*/

    /*prevState é uma referência ao estado anterior. */
    this.setState((prevState, props) => ({
      currentTime: prevState.currentTime + 1
    }));
  }

  /*função invocada quando o componente é renderizado na tela*/
  componentDidMount(){
    /*atributo timerID invoca a função setInterval, que chama a função tick()
    a cada 1000ms (1 segundo)*/
    this.timerID = setInterval(
      (prevState, props) => this.tick(),
      1000
    );
  }

  /*o método render retorna o que será visto pelo HTML*/
  /*Parece HTML, mas ele está retornando JSX*/
  render() {
    return (
      <div>
        <h1>O tempo que se passou em segundos é {this.state.currentTime}.</h1>
      </div>
    );
  }
}

/*o método render é responsável por renderizar os elementos. Ele recebe 3 parâmetros, que são:
o elemento a ser criado, o local em que será inserido no DOM (o conteiner) e uma função
de callback, invocada após a renderização*/
ReactDOM.render(
  <Timer />,
  document.getElementById('principal')
);
