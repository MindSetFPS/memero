export const infiniteScrollObserver = ({ fetch, observedElement }) => {
    if (observedElement) {
      const observer = new IntersectionObserver((entries) => {
        const first = entries[0];
        if (first.isIntersecting) {
          fetch();
        }
      });
  
      observer.observe(observedElement);
    }
  };